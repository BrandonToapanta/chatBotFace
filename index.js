const express = require('express')
const bodyParser = require('body-parser')

const app = express().use(bodyParser.json())

app.post('/webhook', (req, res) => {
    console.log('POST: webhook')

    const body = req.body

    if (body.object === 'page') {

        body.entry.array.forEach(entry => {
            // resibe los mensajes
            const webhookEvent = entry.messaging[o];
            console.log(webhookEvent)
        });

        res.status(200).send('Evento recibido')

    } else {

        res.sendStatus(404)

    }
})
app.get('/webhook', (req, res) => {
    console.log('GET: webhook')

    const Verify_token = 'stringUnicoParaElBot'

    const mode = req.query['hub.mode']
    const token = req.query['hub.verify_token']
    const challenge = req.query['hub.challenge']

    if (mode && token) {
        if (mode === 'subscribe' && token === Verify_token) {

            console.log('webhok verificado')
            res.status(200).send(challenge)

        } else {

            res.sendStatus(404)

        }
    } else {
        res.sendStatus(404)

    }

})

app.listen(3000, () => {
    console.log('servidor iniciado...')
})