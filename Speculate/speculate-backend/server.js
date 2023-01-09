import express from 'express';
import mongoose from 'mongoose';
import cors  from 'cors';
import { ApolloServer } from 'apollo-server-express';
import typeDefs from './graphql/typeDefs.js';
import resolvers from './graphql/resolvers.js';

// app config
const app = express();
// const port = process.env.PORT || 9000;
const port = 9000;


// middleware
app.use(express.json());
app.use(cors());

const server = new ApolloServer({
    typeDefs,
    resolvers
});
await server.start();
server.applyMiddleware({ app });

app.listen({ port }, () => {
    console.log(`Apollo Server on http://localhost:${port}/graphql`);
  });
  

// DB config
const connection_url = 'mongodb+srv://admin:sB0rfdzGIFP3vpii@cluster0.q8nbtet.mongodb.net/?retryWrites=true&w=majority';

mongoose.connect(connection_url, {
  useNewUrlParser: true,
  dbName: 'speculatedb',
}).then(() => {
    console.log("MongoDB Connection successful");
})

  
  

// const db = mongoose.connection;

// db.on('error', console.error.bind(console, 'connection error:'));

// db.once('open', function() {
//   console.log('Connected to MongoDB');
// });

// const message = new Message({ content: 'Hello World' });
// message.save((error) => {
//   if (error) {
//     console.log(error);
//   } else {
//     console.log('Saved to MongoDB');
//   }
// });

// Message.find((error, messages) => {
//   console.log(messages);
// });

// pubsub.publish('messageAdded', { messageAdded: message });


// ----------------------------------------------------------------
// async function connect() {
//     try{
//         await mongoose.connect(connection_url,{
//             bufferCommands: false,
//             dbName: 'speculatedb',
//             user: 'admin',
//             pass: 'sB0rfdzGIFP3vpii',
//             autoIndex: false,
//             autoCreate: true,
//         });
//         console.log("sucess");
//     }
//     catch (error) {
//         console.error(error);
//     }
// };

// connect();

// // ?????

// // api routes
// app.get('/', (req,res) => res.status(200).send('Sucess'));

// app.get('/api/sync', (req, res) => {
//     Subjects.find((err, data) => {
//         if(err) {
//             res.status(500).send(err)
//         } else {
//             res.status(200).send(data)
//             console.log(data)
//         }
//     });
// });

// app.post('/api/new', (req, res) => {
//     const dbMessage = req.body

//     Subjects.create(dbMessage, (err, data) => {
//         if (err) {
//             res.status(500).send(err);
//             console.error(err);
//         } else{
//             res.status(201).send(data);
//         }
//     });
// });
// // listen
// app.listen(port, () => console.log(`Listening on localhost:${port}`));