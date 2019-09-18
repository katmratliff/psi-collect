const public_ip = require('public-ip');
const fs = require('fs');

module.exports = (async function() {
    const yargs = await require('yargs').argv
    const USE_LOCALHOST = yargs.localhost || false
    //If we have the cl arg of host,use machines IP, else use localhost
    const IP = USE_LOCALHOST? 'localhost': await public_ip.v4()
    //Becuase the website and server will have diff ports.
    const PORT_WEB=3000
    const PORT_NODE=4000
    //Following the above comment,we need to generate diff ips with diff ports.
    const SITE_IP = {
        node: `${IP}:${PORT_NODE}`,
        web: `${IP}:${PORT_WEB}`
    }
    //Test to see if fnc can be exported
    async function show_routes(args={})
    {   
        console.log(app_express._router.stack)
        
    }
    //Export these vars n shit.
    return { 
        IP,
        PORT_WEB ,
        PORT_NODE,
        SITE_IP,
        show_routes
    };

})();
