// include dependencies
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const { PORT = 3000 } = process.env;
// create the proxy
/** @type {import('http-proxy-middleware/dist/types').RequestHandler<express.Request, express.Response>} */

// const beUsersProxy = createProxyMiddleware({
//   target: 'http://localhost:8091', // target host with the same base path
//   changeOrigin: true, // needed for virtual hosted sites
//  // pathRewrite: {'^/' : '/users/'},
//   on: {
//     proxyReq: (proxyReq, req, res) => {
//       console.log('beUsersProxy req',proxyReq.originalUrl );
//       console.log('beUsersProxy req',req.originalUrl );
//     },
//     },
// });

const chat = createProxyMiddleware({
  target: 'http://localhost:3006', // target host with the same base path
  
  changeOrigin: true, // needed for virtual hosted sites
});
const rewriteFn = function (path, req) {
  console.log('rewriteFn',path );
  return path;
};
const rasa = createProxyMiddleware({
  target: 'http://localhost:5005', // target host with the same base path
  changeOrigin: true, // needed for virtual hosted sites
  pathRewrite: rewriteFn,
  on: {
    proxyReq: (proxyReq, req, res) => {
      console.log('rasa req',proxyReq.originalUrl );
      console.log('rasa req',req.originalUrl );
       // log the search request
       let bodyData = '';
       

       res.on('data', (chunk) => {
         bodyData += chunk;
       });
       res.on('end', async () => {
         console.log('rasa req',bodyData );
       });
      //console.log('rasa req',res );
    },
    proxyRes: (proxyReq, req, res) => {
      console.log('rasa resp',proxyReq.originalUrl );
      console.log('rasa resp',req.originalUrl );
      let bodyData = '';
       

       res.on('data', (chunk) => {
         bodyData += chunk;
       });
       res.on('end', async () => {
         console.log('rasa req',bodyData );
       });
    //console.log('rasa req',res );
    },
    },
});


app.use('/rasa', rasa);
app.use('/', chat);

app.listen(PORT, () => console.log(`Proxy API server started at port ${PORT}`));