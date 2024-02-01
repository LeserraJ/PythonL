const app = require('express')();
const PORT = 8000;

app.listen(
    PORT,
    () => console.log('Port Live on http://localhost:${PORT}')
)

app.get('/nations', (req, res) =>{
    res.status(200).send({
        usa: ("tanks", "planes"),
        germany:("tanks", "planes"),
        russia:("tanks", "planes"),
        britian:("tanks", "planes"),
        france:("tanks", "planes"),
        italy:("tanks", "planes"),
        sweden:("tanks", "planes"),
        israel:("tanks", "planes"),

    })
});

app.get('/usa/tanks', (req, res) =>{
    res.status(200).send({
        rank:("rank_1","rank_2","rank_3","rank_4","rank_5","rank_6","rank_7")
    })
});

app.get('/usa/tanks/rank_1', (req,res) =>{
    res.status(200).send({
        1: ("M2A4"),
        1.3: ("M2")
    })
});