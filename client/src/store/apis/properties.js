import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const propertiesApi = createApi({
  reducerPath: "propertiesApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1/properties/",
    prepareHeaders: (headers) => {
      headers.append(
        "Authorization",
        "Bearer " +
          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3MzQzNDkzLCJpYXQiOjE3MDczMzYyOTMsImp0aSI6IjM5N2FjODExNDhmMzQ4OWViYjcwYmU0YWVjNzA2Y2JlIiwidXNlcl9pZCI6OH0.QNR7szdcG9TUhCpDsGyIRLA3mKD8acs7fekLk9pC3yI"
      );

      return headers;
    },
  }),
  endpoints: (builder) => ({
    getProperties: builder.query({
      query: () => {
        return {
          url: "",
          method: "GET",
          credentials: "include",
        };
      },
    }),
    getRealtorProperties: builder.query({
      query: () => {
        return {
          url: "realtor",
          method: "GET",
          credentials: "include",
        };
      },
    }),
    addProperty: builder.mutation({
      query: (property) => {
        console.log(property);
        return {
          url: "create",
          method: "POST",
          body: {
            property,
          },
          credentials: "include",
        };
      },
    }),
  }),
});

export const {
  useGetPropertiesQuery,
  useGetRealtorPropertiesQuery,
  useAddPropertyMutation,
} = propertiesApi;
