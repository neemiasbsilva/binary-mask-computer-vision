from binary_mask import binary_mask
from show_b_mask import show_b_mask


def main():

    print("Choose the path of image for binarize:", end=' ')
    path = str(input())
    print("Choose the value of parameter r:", end=' ')
    r = float(input())
    print("Choose the value of parameter g:", end=' ')
    g = float(input())
    print("Choose the value of parameter b:", end=' ')
    b = float(input())
    print("Choose the value of parameter k:", end=' ')
    k = float(input())

    img_original, img_binary = binary_mask(path, r, g, b, k)    

    # visualize the result using the binary mask technique
    show_b_mask(img_original, img_binary)
    
if __name__ == "__main__":
    main()