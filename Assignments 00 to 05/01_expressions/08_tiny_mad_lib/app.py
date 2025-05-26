def main():
    adjective = input("Ek adjective daalain (jaise: purple): ")
    noun = input("Ek noun daalain (jaise: treehouse): ")
    verb = input("Ek verb daalain (jaise: nachna ya gana): ")


    story = f"Ek lazy bandar (🐒) subah der se utha aur seedha ek {noun} mein chala gaya.\
Woh wahan baith kar {adjective} chhatri ke neeche {verb} shuru ho gaya!"
    
    print(story)


if __name__ == '__main__':
    main()