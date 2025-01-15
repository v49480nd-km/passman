package main

import ("fmt")

func start_msg_cli() {
    fmt.Println("PASSMAN")
    fmt.Println("[1] Generate Password")
    fmt.Println("[2] List Passwords")
    fmt.Println("[3] Delete Password")
}

func main() {
    fmt.Println("Hello world")

    start_msg_cli()
}
