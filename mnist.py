import numpy as np

class Mnist:
    def __init__(self, path, train=True):
        if train:
            image_file_name = "train-images.idx3-ubyte"
            label_file_name = "train-labels.idx1-ubyte"
        else:
            image_file_name = "t10k-images.idx3-ubyte"
            label_file_name = "t10k-labels.idx1-ubyte"
            
        self.f = open("{}//{}".format(path, image_file_name), "rb")
        magic_number, number_of_images, image_rows, image_columns = int(self.f.read(4).hex(), 16), \
        int(self.f.read(4).hex(), 16), int(self.f.read(4).hex(), 16), int(self.f.read(4).hex(), 16)
        print("Images magic no: {},  No of images: {}, Image rows: {}, Image cols: {}".\
          format(magic_number, number_of_images, image_rows, image_columns))

        self.flab = open("{}//{}".format(path, label_file_name), "rb")
        magic_number, number_of_items = int(self.flab.read(4).hex(), 16), int(self.flab.read(4).hex(), 16)
        print("Labels magic no: {}, No of items: {}".format(magic_number, number_of_items))
        

    def _get_next(self):
        val = self.f.read(28*28)
        if len(val)>0:
            img = val.hex()
            idxs = np.arange(0, len(img), 2).astype(int)
            return(np.reshape([int(img[i:(i+2)], 16) for i in idxs], (28, 28)), int(self.flab.read(1).hex(), 16)) 
        else:
            return("", "")

    def get_batch(self, batch_size=20, scale=True):
        im_lst = np.zeros(shape=[batch_size, 28, 28], dtype="float")
        lbl_lst = np.zeros(shape=[batch_size], dtype="int")
        lbl_one_hot_lst = np.zeros(shape=[batch_size, 10], dtype="int")
        for i in range(batch_size):
            im, lbl = self._get_next()
           
            if len(im)>0:
                if scale:
                    im=im/255.
                im_lst[i,...] = im
                lbl_lst[i] = lbl
                lbl_one_hot_lst[i,lbl] = 1
        return im_lst, lbl_lst, lbl_one_hot_lst

