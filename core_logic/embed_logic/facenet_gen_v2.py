# embed_logic/facenet_gen_v2.py

from keras.models import load_model
import numpy as np
from .gen_base_final import EmbedBase

class FacenetGenFinal(EmbedBase):
    def __init__(self, model_path=None):
        super().__init__()
        self.model_final = load_model(model_path or 'facenet_keras.h5')

    def load_mod_final(self, path=None):
        """
        Load the FaceNet model from the specified path.
        """
        self.model_final = load_model(path or 'facenet_keras.h5')

    def gen_embedding_final(self, face_pixels):
        """
        Generate a 128-dimensional embedding for a face.
        """
        face_pixels = self.prep_pixels_final(face_pixels)
        embedding = self.model_final.predict(face_pixels)
        return embedding[0]

    def prep_pixels_final(self, face_pixels):
        """
        Standardize pixel values across channels.
        """
        face_pixels = face_pixels.astype('float32')
        mean, std = face_pixels.mean(), face_pixels.std()
        face_pixels = (face_pixels - mean) / std
        return np.expand_dims(face_pixels, axis=0)

    
    def gen_embeddings_for_all_done(self, faces):
        """
        Generate embeddings for multiple faces (not used).
        """
        return [self.gen_embedding_final(face) for face in faces]

"""
# Previous version of gen_embedding_final that didn’t work as intended
def gen_embedding_almost(face_pixels):
    face_pixels = face_pixels.astype('float32')
    face_pixels = (face_pixels - face_pixels.mean()) / face_pixels.std()
    face_pixels = np.expand_dims(face_pixels, axis=0)
    embedding = self.model_final.predict(face_pixels)
    return embedding[0]
"""


def run_embedding_pipeline(face_img):
    generator = FacenetGenFinal()
    embedding = generator.gen_embedding_final(face_img)
    print(f"Generated embedding: {embedding}")
    return embedding
