import { FaHeartCrack } from "react-icons/fa6";
import { Container, Row, Col } from "react-bootstrap";
import SEO from "../components/shared/SEO";

const NotFound = () => {
  return (
    <>
      <SEO
        title="RealMaison real estate"
        description="page you are looking for is not found"
      />

      <Container>
        <Row>
          <Col className="text-center">
            <h1 className="notfound">404 Not Found</h1>
            <h3>The page you are looking for does not exist.</h3>
            <FaHeartCrack style={{ fontSize: 50, color: "#da0c81" }} />
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default NotFound;
