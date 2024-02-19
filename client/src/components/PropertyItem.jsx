import { useNavigate } from "react-router-dom";
import { Col, Row, Badge, Card, Button, CardTitle } from "react-bootstrap";
import { FaShower, FaBed, FaChartArea } from "react-icons/fa";
import SEO from "./shared/SEO";

const spansStyle = {
  marginRight: "5px",
};

const PropertyItem = ({ property }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/details/${property.slug}`);
  };

  return (
    <>
      <SEO title={property.title} description={property.description} />

      <Card style={{ width: "18rem", height: "100%", position: "relative" }}>
        <Badge className="position-absolute start-100 top-0 translate-middle rounded-pill ">
          {property.sale_type}
        </Badge>
        <Card.Img
          style={{ width: "100%", maxHeight: "200px", objectFit: "cover" }}
          variant="top"
          src={
            property.images.length > 0
              ? property.images[0].image
              : "default-image-url"
          }
        />

        <CardTitle>{property.price}€</CardTitle>
        <Card.Body style={{ overflowY: "auto" }}>
          <Card.Title as="h4">
            <strong>{property.title}</strong>
          </Card.Title>
          <Card.Text as="p">
            {property.description.substring(0, 100)}...
          </Card.Text>
          <hr />
          <Row>
            <Col style={{ display: "flex", justifyContent: "space-evenly" }}>
              <span>
                <FaBed style={spansStyle} />
                {property.bedrooms}
              </span>
              <span>
                <FaShower style={spansStyle} />
                {property.bathrooms}
              </span>
              <span>
                <FaChartArea style={spansStyle} />
                {property.surface}m²
              </span>
            </Col>
          </Row>
          <hr />
          <Button
            style={{
              backgroundColor: "#da0c81",
            }}
            onClick={handleClick}
          >
            More info
          </Button>
        </Card.Body>
      </Card>
    </>
  );
};

export default PropertyItem;
