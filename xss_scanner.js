let payload = "<script>alert(1)</script>";
let urls = ["/search?q=", "/profile?name="];
urls.forEach(u => fetch(u + payload));
