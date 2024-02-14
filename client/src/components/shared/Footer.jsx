import { Container, Col, Row } from "react-bootstrap";

const Footer = () => {
  return (
    <footer style={{ backgroundColor: "black", color: "white" }}>
      <Container>
        <Row>
          <Col>
            <p>Copyright &copy; RealMaison {new Date().getFullYear()} </p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
