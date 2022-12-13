import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder

class IrisService(object):
    def __init__(self):
        model = load_model('./save/iris_model.h5')
        graph = tf.get_default_graph()
        target_names = datasets.load_iris().target_name

    def hook(self):
        # self.spec()
        self.service_model()

    def service_model(self):
        pass


        '''
        Shape (150, 6)
        'Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 
        'PetalWidthCm', 'Species'
        '''

iris_menu = ["Exit",  # 0
               "Learning",  # 1
               ]

iris_lambda = {
    "1": lambda x: x.hook(),
    }

if __name__ == '__main__':
    Iris = IrisService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](Iris)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")