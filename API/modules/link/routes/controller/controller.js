const fs = require("fs");//The fs module enables interacting with the file system(json file).
const path = require("path");//The path module provides utilities for working with file and directory paths.

const filePath = path.join(__dirname, "../../../../DB/dbUsers.json");
const indexPath = path.join(__dirname, "http://localhost:3000/index.html");
//__dirname to get url from c to controller file
//path.join resolve location from c to "../../../../DB/dbUsers.json"

//get handler -- to get data save in varible getLinks.
const getLinks = (req, res, next) => {
    //read data from json file.
    const links = JSON.parse(
        fs.readFileSync(filePath)
    );
    res.json({ message: "sucsess", data: links });//send the response by json.
};
//and links in json file
const addLinks = (req, res, next) => {
    //save data in array 
    const links = JSON.parse(
        fs.readFileSync(filePath)
    );
    const { link } = req.body;//distract link from body.
    //create an object (assignObj)  to save link and id in it  
    const assignObj = {
        id: links.length,
        link
    }

    //check link exist or no  
    const findLink = links.find((ele) => {
        return ele.link == link;
    })
    //check frontEnd devloper send data in varible (link) or no
    if (!link) {
        res.json({ message: "error : send on link variable" })
    }
    //link exist?
    else if (findLink) {
        res.json({ message: "error : is exist" })
    }
    //svae data in obj (assignObj)
    else {
        links.push(assignObj);
    }
    //write in json file
    fs.writeFileSync(filePath, JSON.stringify(links));
    res.json({ message: "sucsess data send to API", link: links })
};
// data send by software developer
const addcheck = (req, res, next) => {
    const users = JSON.parse(
        fs.readFileSync(filePath)
    );
    const { link, check } = req.body;

    //check (check -->(check on link)) exist or no
    let findCheck = users.find((ele) => {
        return ele.check == check;
    })
    //check link exist or no
    let findLink = users.find((ele) => {
        return ele.link == link;
    })
    const assignObj = {
        id: users.length - 1,
        link,
        check
    }
    //check frontEnd devloper send data in varible (link or check) or no
    if (!link || !check) {
        res.json({ message: "error : Make sure you send dat in link and check variable" })
    }
    //Check if (link  and Check) exist ?
    //note : the same link and Check --> is send again
    else if (findCheck && findLink) {
        res.json({ message: "the same error" })
    }
    //save data in json file
    else {
        users.push(assignObj);
    }
    fs.writeFileSync(filePath, JSON.stringify(users));
    res.json({ message: "sucsess data send to API", link: users })
};
// make all object use in another files

module.exports = {
    getLinks,
    addLinks,
    addcheck
}