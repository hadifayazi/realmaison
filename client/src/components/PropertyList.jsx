import { useGetPropertiesQuery } from "../store/index";
import PropertyItem from "./PropertyItem";

const PropertyList = () => {
  const { data, error, isLoading, isSuccess } = useGetPropertiesQuery();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!isSuccess) return <div>Error: {JSON.stringify(data)}</div>;

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        maxWidth: "300px",
        padding: "20px",
      }}
    >
      {data?.results?.map((property) => (
        <PropertyItem key={property.id} property={property} />
      ))}
    </div>
  );
};

export default PropertyList;
