import { useNavigate } from "react-router-dom";

const PropertyItem = ({ property }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/details/${property.slug}`); // Use history.push to navigate to the "/details" route
  };

  return (
    <button
      onClick={handleClick}
      style={{
        maxWidth: "300px",
        border: "2px dashed red",
      }}
    >
      <div>{property.title}</div>
      <div>{property.reference}</div>
      <div>{property.description}</div>
      <div>{property.city}</div>
      <div>{property.house_type}</div>
      <div>{property.price}</div>
    </button>
  );
};

export default PropertyItem;
