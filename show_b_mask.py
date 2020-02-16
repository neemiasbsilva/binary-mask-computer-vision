import matplotlib.pyplot as plt


def show_b_mask(img_original, img_binary):
    plt.figure(1, figsize=(10, 10))
    
    # Plot the Original image
    plt.subplot(121)
    plt.imshow(img_original)
    plt.title("Original Image")
    plt.axis('off')
    # Plot the Binary image
    plt.subplot(122)
    plt.imshow(img_binary)
    plt.title("Binary Image")
    plt.axis('off')