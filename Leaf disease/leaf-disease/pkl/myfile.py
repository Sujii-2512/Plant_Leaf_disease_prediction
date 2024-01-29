import pickle
leaflist=['tomato','brinjal','raddish']
with open('cnn_model.pkl','wb') as leafpickle:
	pickle.dump(leaflist,leafpickle)