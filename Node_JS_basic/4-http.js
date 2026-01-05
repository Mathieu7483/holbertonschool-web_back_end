http=require("http")

app=http.createServer()
app.on("request",(req,res)=>{
    res.writeHead(200,{'Content-Type':'text/plain'})
    res.end("Hello Holberton School!")
})
app.listen(1245, ()=>{
    console.log("Server is listening on port 1245")
})
