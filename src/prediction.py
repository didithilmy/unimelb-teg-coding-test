import pickle
import io
import numpy as np
from config import MODEL_PATH

class ModelPrediction:
    def predict(self, input_file):
        X_te = np.genfromtxt(input_file, delimiter=',')
        with open(MODEL_PATH, 'rb') as f:
            net, scaler = pickle.load(f) 
            test_preds = net.predict(np.hstack([scaler.transform(X_te[:,:8]), X_te[:,8:]])) #predict using test features

            out_stream = io.BytesIO()
            np.savetxt(out_stream, test_preds, delimiter=",")
            return out_stream