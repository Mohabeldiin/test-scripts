const { getLinks, addLinks, addcheck } = require("../controller/controller")//distract the varible we want to use it from folder controller
const router = require("express").Router()//to use locatoin of varible wit HTTP protocol method (shuch as :getLinks with GET method)

//we use varible that we distract it  to make handler in another file 
router.get("/getLinks", getLinks)

router.post("/addLinks", addLinks)
router.post("/addcheck", addcheck)

module.exports = router // make all another files allow to accsess router to see it when require