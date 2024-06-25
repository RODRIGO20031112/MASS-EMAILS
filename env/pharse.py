def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def create_gradient(text, start_rgb, end_rgb):
    n = len(text)
    gradient_text = ""
    
    for i, char in enumerate(text):
        r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i // n
        g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i // n
        b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i // n
        gradient_text += f"{rgb_to_ansi(r, g, b)}{char}"
    
    return gradient_text + "\033[0m"  

def createPharse():
    phrase = """
       _____                                                 .__.__          
      /     \    __    ______ ______     ____   _____    __  |__|  |   ______
     /  \ /  \  /__\  /  ___//  ___/   _/ __ \ /     \  /__\ |  |  |  /  ___/
    /    Y    \/ __ \_\___ \ \___ \    \  ___/|  Y Y  \/ __ \|  |  |__\___ \ 
    \____|__  (____  /____  >____  >    \___  >__|_|  (____  /__|____/____  >
            \/     \/     \/     \/         \/      \/     \/             \/                                                   
    """

    start_color = (255, 0, 0)
    end_color = (0, 255, 0)

    gradient_phrase = create_gradient(phrase, start_color, end_color)

    return(gradient_phrase)