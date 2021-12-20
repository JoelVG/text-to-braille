import React, { Component, Fragment, Container } from "react";

export default class Process extends Component {
    render() {
        console.log("entro a la function");

        return (
            <div className="App">
              <header className="App-header">
              </header>
              <body>
                <Fragment>
                <Container fixed>
                <p style={{backgroundColor: "green"}}>holi again</p>
                </Container>
                </Fragment>
              </body>
            </div>
        );
    }
}