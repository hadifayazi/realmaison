import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { Link } from "react-router-dom"; // Import Link from react-router-dom

function Header() {
  return (
    <>
      <Navbar style={{ backgroundColor: "#000000" }} variant="dark" expand="md">
        <Container>
          <Link to="/" className="logo" style={{ color: "white" }}>
            Real<span style={{ color: "#da0c81" }}>M</span>aison
          </Link>
          <Navbar.Toggle aria-controls="navbar-nav" />
          <Navbar.Collapse id="navbar-nav">
            <Nav className="me-auto">
              <Link to="/properties" className="nav-link">
                Properties
              </Link>
              <Link to="/realtors" className="nav-link">
                Realtors
              </Link>
              <Link to="/about" className="nav-link">
                About us
              </Link>
              <Link to="/contact" className="nav-link">
                Contact
              </Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;
