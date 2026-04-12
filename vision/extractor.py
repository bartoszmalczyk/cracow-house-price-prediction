from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import logging
from transformers import logging as hf_logging

hf_logging.set_verbosity_error()

clip_id = "openai/clip-vit-base-patch32"
clip_processor = CLIPProcessor.from_pretrained(clip_id)
clip_model = CLIPModel.from_pretrained(clip_id)

def is_interior(img_path):
    """
    This function will simply checks if photos contains only interior
    (we do not want photos of buildings or 2D plans)
    """
    try:
        image = Image.open(img_path).convert("RGB")
        categories = [
            "a photo of a residential apartment interior room",
            "a photo of a building exterior or street",
            "a 2d architectural floor plan or layout drawing"
        ]
        inputs = clip_processor(text=categories, images=image, return_tensors="pt", padding=True)
        outputs = clip_model(**inputs)

        logits_per_image = outputs.logits_per_image
        probabilities = logits_per_image.softmax(dim=1).detach().numpy()[0]
        interior_score = probabilities[0]  
        exterior_score = probabilities[1] 
        interior_threshold = 0.80

        if interior_score >= interior_threshold:
            return True 
        else:
            return False 
                
    except Exception as e:
        print(f"Failed to verify {img_path}: {e}")
        return False
    
print(is_interior("2_2_pgpwmk.jpg"))
