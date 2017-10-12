# -*- coding: UTF-8 -*-
'''
Kunwang, created on October 12th, 2017
'''

import unittest
from OImageUtil import O_ImageUtil
from PIL import Image

class TestOImageUtil(unittest.TestCase):
    #Use the dedicated folder to hold the resources for testing.
    def load_resource(self, filename):        
        f_path = r".\resources\%s" % (filename)
        return Image.open(f_path)

    def test_ocrImage_with_string(self):
        util = O_ImageUtil()
        filename = r"150527133311.jpg"
        img = self.load_resource(filename)
        self.assertEqual("Display Date/Time", util.ocrImage(img))
        return

    def test_ocrImage_with_time(self):
        util = O_ImageUtil()
        filename = r"150527141221.jpg"
        img = self.load_resource(filename)
        self.assertEqual("10:45", util.ocrImage(img))
        return

    def test_ocrImage_with_cropped_region(self):
        util = O_ImageUtil()
        filename = r"150527141164.jpg"
        img = self.load_resource(filename)
        region = (430, 740, 572, 806)
        img_region = img.crop(region)
        self.assertEqual("10:45", util.ocrImage(img_region))
        return
    
    def test_ocr_netflix(self):
        util = O_ImageUtil()
        filename = r"150527133153.jpg"
        img = self.load_resource(filename)        
        self.assertEqual("Deactivate Netflix", util.ocrImage(img))
        return
    
    def test_ocr_netflix_unicode(self):
        util = O_ImageUtil()
        filename = r"150527133153.jpg"
        img = self.load_resource(filename)        
        self.assertEqual(u'Deactivate Netﬂix', util.ocrImage(img))
        return

    def test_overlay_image(self):
        img1 = self.load_resource(r"foroverlap_1.jpg")
        img2 = self.load_resource(r"foroverlap_2.jpg")      
        util = O_ImageUtil()  
        img_overlap = util.overlayImage(img1, img2)
        saved_file = r".\resources\overlap.jpg"
        img_overlap.save(saved_file, quality = 99)

    def test_overlay_image_with_none(self):
        img1 = self.load_resource(r"foroverlap_1.jpg")
        img2 = None
        util = O_ImageUtil()
        with self.assertRaises(ValueError):
            util.overlayImage(img1, img2)
            
    def test_overlay_image_with_different_size(self):
        img1 = self.load_resource(r"foroverlap_1.jpg")
        img2 = self.load_resource(r"150527141164.jpg")
        util = O_ImageUtil()
        with self.assertRaises(ValueError):
            util.overlayImage(img1, img2)

    def test_diff_image_with_same_images(self):
        img1 = self.load_resource(r"150527133311.jpg")
        img2 = self.load_resource(r"foroverlap_1.jpg")
        util = O_ImageUtil()
        self.assertEqual(0.0, util.diffImage(img1, img2))

    def test_diff_image_with_different_images(self):
        img1 = self.load_resource(r"img_diff_1.jpg")
        img2 = self.load_resource(r"img_diff_2.jpg")
        util = O_ImageUtil()
        self.assertGreater(150, util.diffImage(img1, img2))


    #method to do dummy test
    def test_debug_method(self):
        #TODO(write your debug code here before move it to the real test-method)
        return
    

if __name__ == "__main__":
    unittest.main()
        
        
        
        
