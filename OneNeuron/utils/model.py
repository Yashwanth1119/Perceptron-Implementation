import numpy as np 

class Perceptron:
    def __init__(self, eta, epochs):
        ##np.random.seed(42) # GIVES SIMILIAR RESULT
        self.weights = np.random.randn(3) * 1e-4 #small weight intializing 
        print(f"intial weights before training: \n{self.weights}")
        self.eta = eta # learning rate
        self.epochs = epochs
        
        
    def activationFunction(self, inputs, weights):
        z = np.dot(inputs, weights) # z = W * X
        return np.where(z > 0, 1, 0) # CONDITION, IF TRUE, ELSE
        
    
    def fit(self, X, y):
        self.X = X
        self.y = y
        
        X_with_bias = np.c_[self.X, -np.ones((len(self.X), 1))] # concatination
        print(f"X with bias: \n{X_with_bias}")
        
        for epoch in range(self.epochs):
            print("--"*10)
            print(f"for epoch: \n{epoch}")
            print("--"*10)
            
            y_hat = self.activationFunction(X_with_bias, self.weights) #FORWARD PROPOGATION 
            print(f"predicted value after forward pass: \n{y_hat}")
            self.error = self.y - y_hat # predicted value y_hat
            print(f"error: {self.error}")
            self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error) # BACKWARD PROPOGATION
            print(f"updated weights after epoch: \n{epoch}/{self.epochs} :{self.weights}")
            print("####"*10)
            
    def predict(self, X):
        X_with_bias = np.c_[X, -np.ones((len(X), 1))] 
        return self.activationFunction(X_with_bias, self.weights)
        
    def total_loss(self):
        total_loss = np.sum(self.error)
        print(f"total loss: \n{total_loss}")
        return total_loss
        