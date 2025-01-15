package main

import ("fmt")

func start_msg_cli() {
    fmt.Println("PASSMAN")
    fmt.Println("[1] Generate Password")
    fmt.Println("[2] List Passwords")
    fmt.Println("[3] Delete Password")
    fmt.Print("> ")
}

func main() {
    start_msg_cli()
    
    var user_option int
    fmt.Scanf("%v", &user_option)

    switch user_option {
    case 1:
        fmt.Println("printing password") 
    case 2:
        fmt.Println("listing poasswords")
    case 3:
        fmt.Println("deleting password")
    default:
        fmt.Println("Not an option playboy")
    }
}
