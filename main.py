from file_handler import FileHandler
from launch_squad import run_squad

def main():
    ini_dir = FileHandler()

    norm_exist = ini_dir.does_ini_file_exist("normal")
    seed_exist = ini_dir.does_ini_file_exist("seed")

    menu = f"""
    SNEED TOOL V2 
    OPTIONS: 
    0) Exit program. 
    1) Make new seed file. [Exists: {seed_exist}] 
    2) Make/update normal file. [Exists: {norm_exist}] 
    3) Run game with seed settings. 
    4) Run game with normal settings. 
    """
    count = 0
    print(menu)
    while True and count < 20:
        user_input = input("Option: ")
        match user_input:
            case "0":
                break
            case "1":
                ini_dir.create_seed_ini()
            case "2":
                ini_dir.create_normal_ini()
            case "3":
                ini_dir.switch_ini("seed")
                run_squad()
            case "4":
                ini_dir.switch_ini("normal")
                run_squad()
            case _:
                print("Invalid option.")
        print(menu)
        count = count + 1

if __name__ == "__main__":
    main()