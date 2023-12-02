custom_domains = {
    "proxy": [
        "",
    ],
    "direct": [
        "",
    ],
    "remove": [
        "googleapis.com",
        "gvt1.com",
        "eset.com",
        "ubuntu.com",
        "radiojavan.com",
        "github.io",
        "wordpress.com",
    ],
    "remove_contain": [
        "google.com",
        "ooklaserver.net",
    ],
    "remove_regex": [
        r"^vn",
    ],
}

if __name__ == "__main__":
    import json
    print(json.dumps(custom_domains))
