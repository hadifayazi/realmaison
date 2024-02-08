import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { Link } from "react-router-dom";

function Header() {
  return (
    <>
      <Navbar style={{ backgroundColor: "#FFB3B3" }} variant="dark" expand="md">
        <Container>
          <Navbar.Brand href="#home">RealMaison</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbar-nav" />
          <Navbar.Collapse id="navbar-nav">
            <Nav className="me-auto">
              <Link to="/">Properties</Link>
              <Nav.Link href="#features">Realtors</Nav.Link>
              <Link to="/about">About us</Link>
              <Nav.Link href="#pricing">Contact</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;
