import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

function Header() {
  return (
    <>
      <Navbar style={{ backgroundColor: "#000000" }} variant="dark" expand="md">
        <Container>
          <Navbar.Brand className="logo" href="/">
            Real<span style={{ color: "#da0c81" }}>M</span>aison
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="navbar-nav" />
          <Navbar.Collapse id="navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/properties">Properties</Nav.Link>
              <Nav.Link href="/realtors">Realtors</Nav.Link>
              <Nav.Link href="/about">About us</Nav.Link>
              <Nav.Link href="/contact">Contact</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;
