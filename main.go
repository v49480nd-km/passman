package main

import ("fmt")

func start_msg_cli() {
    var msg_list = [4]string{
        "PASSMAN",
        "[1] Generate Password",
        "[2] List Passwords",
        "[3] Delete Password"
    }

    for i := 0; i < 4; i++ {
        fmt.Println(msg_list[i])
    }
}

func main() {
    start_msg_cli()
}
