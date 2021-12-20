import React, { Component } from "react";
import Container from '@material-ui/core/Container';
import { Fragment } from 'react';
import { Button } from '@material-ui/core';
import Process from "./Process";

class Home extends Component {
    render() {
        return (
            <div className="App">
              <header className="App-header">
              </header>
              <body>
                <Fragment>
                <Container fixed>
                  <p>Bienvenido a texto-braille</p>
                  <Button style={{marginTop: "50px"}} onClick={<Process/>} variant="contained" color="primary">
                    Iniciar
                  </Button>
                </Container>
                </Fragment>
              </body>
            </div>
        );
    }
}

export default Home