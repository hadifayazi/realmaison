import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

function Header() {
  return (
    <>
      <Navbar style={{ backgroundColor: "#FFB3B3" }} variant="dark" expand="md">
        <Container>
          <Navbar.Brand href="#home">RealMaison</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbar-nav" />
          <Navbar.Collapse id="navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#home">Properties</Nav.Link>
              <Nav.Link href="#features">Realtors</Nav.Link>
              <Nav.Link href="#pricing">About us</Nav.Link>
              <Nav.Link href="#pricing">Contact</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;
