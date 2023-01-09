import Billboard from './compents/Billboard';
// import Footer from './compents/Footer';
import Navbar from './compents/Navbar'
// import Login from './compents/Login'
import { ApolloClient, ApolloProvider, InMemoryCache } from '@apollo/client';
// import APIs from './APIs'
const API = new ApolloClient({
  uri:"http://localhost:9000/graphql",
  cache: new InMemoryCache(),
});


function App() {
  return (
  <>
    <ApolloProvider client={API}>
      {/* <Login/> */}
      <Navbar />
      <Billboard/>
      {/* <Footer /> */}
    </ApolloProvider>
  </>
  );
}

export default App;
