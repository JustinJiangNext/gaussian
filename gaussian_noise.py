import cv2
from multiprocessing import Process
import numpy as np



def add_gaussian_noise(input_image_path, output_image_path, mean=0, std_dev=25):
    # Load the color image
    image = cv2.imread(input_image_path)
    
    # Check if the image was loaded properly
    if image is None:
        print(f"Error: Could not load image at {input_image_path}")
        return
    
    # Generate Gaussian noise for each color channel (512x512x3)
    gaussian_noise = np.random.normal(mean, std_dev, image.shape).astype(np.float32)
    
    # Add Gaussian noise to the image
    noisy_image = image.astype(np.float32) + gaussian_noise
    
    # Clip the pixel values to stay within the valid range
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    
    # Save the noisy image
    cv2.imwrite(output_image_path, noisy_image)
    print(f"Noisy image saved at {output_image_path}")


def convertFolder(inputPath, outputPath):
    os.system("mkdir " + outputPath)
    for file in os.listdir(inputPath):
        add_gaussian_noise(os.path.join(inputPath, file), os.path.join(outputPath, "noised_" + file))

        print(file)
    print("""
    
    
    """ + inputPath + """
    
    
    
    """)





if __name__ == '__main__':
    print("Main start")
 
    converters = [
        Process(target=convertFolder, args=("loraDataSet1/SD21Airplane", "outputNoise")),
        Process(target=convertFolder, args=("loraDataSet1/SD21Automobile", "outputNoise")),
        Process(target=convertFolder, args=("loraDataSet1/SD21Bird", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Cat", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Deer", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Dog", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Frog", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Horse", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Ship", "outputNoise")),
    	Process(target=convertFolder, args=("loraDataSet1/SD21Truck", "outputNoise")),
    ]

    for worker in converters:
        worker.start()
    for worker in converters:
        worker.join()
    
