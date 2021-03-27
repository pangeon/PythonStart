image_stage_1 = '''    
 |     
/|\\     
'''

image_stage_2 = '''
 |     
 |     
 |    
 |    
/|\\     
'''

image_stage_3 = '''
 _______
 |     
 |     
 |    
 |    
/|\\     
'''

image_stage_4 = '''
 _______
 |     |
 |     O
 |     |
 |    
/|\\     
'''

image_end = '''
 _______
 |     |
 |     O
 |    /|\\
 |    / \\
/|\     
'''


def show_stage_image(amount_of_lives):
    if amount_of_lives == 4:
        print(image_stage_1)
    elif amount_of_lives == 3:
        print(image_stage_2)
    elif amount_of_lives == 2:
        print(image_stage_3)
    elif amount_of_lives == 1:
        print(image_stage_4)
