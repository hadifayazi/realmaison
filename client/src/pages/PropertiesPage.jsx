import { Col, Container, Row } from "react-bootstrap";
import { useGetPropertiesQuery } from "../store/index";
import PropertyItem from "../components/PropertyItem";
import Spinner from "react-bootstrap/Spinner";
import SEO from "../components/shared/SEO";

const PropertiesPage = () => {
  const { data, error, isLoading } = useGetPropertiesQuery();
  return (
    <>
      <SEO title="Properties" description="Catalog of properties" />
      {isLoading ? (
        <Spinner />
      ) : error ? (
        <div>{error.message}</div>
      ) : (
        <Container style={{ height: "900px" }}>
          <Row>
            <Col
              style={{
                display: "flex",
                justifyContent: "space-evenly",
                marginTop: "20px",
                marginBottom: "20px",
              }}
            >
              {data?.results?.map((property) => (
                <PropertyItem key={property.id} property={property} />
              ))}
            </Col>
          </Row>
        </Container>
      )}
    </>
  );
};

export default PropertiesPage;
