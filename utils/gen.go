package gen

import("fmt")

type Generate struct {
    // get from user
    var name string
    var use_nums, use_schars bool
    // predefined 
    var pwd_len int
    var pwd_chars string
    var pwd string
}

func set_pwd_chars(is_nums bool, is_schars bool) string {
    fmt.Println("here is the set of chars")
}

func generate(all_pwd_chars string, length int, password string) string {
    fmt.Println("generating")
}
