//Express is the most popular Node web framework , easy to use HTTP protocol method (GET, POST, DELETE , PUT, PATCH). 
const express = require('express')//require express library.
const app = express()//run function express in variable to use Features of express.
const cors = require('cors')//require cors library to use API on localhost..

//Location of file there is HTTP protocol method (we use it).
const linkModule = require('./modules/link/routes/linkRoute/link')

app.use(express.json())//public middleware --> convert any data to json.
app.use(linkModule)//to use HTTP protocol method. 
app.use(cors())//run function to use local API.
//app.listen to choose where API run on which port.
app.listen(3000, () => {
    console.log('app run on port 3000 !......')
})