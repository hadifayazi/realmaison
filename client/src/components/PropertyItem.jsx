import { useNavigate } from "react-router-dom";
import Card from "react-bootstrap/Card";

const PropertyItem = ({ property }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/details/${property.slug}`); // Use history.push to navigate to the "/details" route
  };

  return (
    <Card style={{ width: "18rem" }}>
      <Card.Img variant="top" src="https://picsum.photos/300/300/?blur" />
      <Card.Body>
        <Card.Title>{property.title}</Card.Title>
        <Card.Text>
          <p className="customParagraph">
            {property.country},{property.city}
          </p>
          <p className="customParagraph">Surface: {property.surface}</p>
          <p className="customParagraph">Bedrooms: {property.bedrooms}</p>
          <p className="customParagraph">Price: {property.price}</p>
          <h6>{property.sale_type}</h6>
        </Card.Text>
        <button onClick={handleClick}>Take a look</button>
      </Card.Body>
    </Card>
  );
};

export default PropertyItem;
