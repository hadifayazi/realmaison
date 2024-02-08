import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const propertiesApi = createApi({
  reducerPath: "propertiesApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1/properties/",
    prepareHeaders: (headers) => {
      headers.append(
        "Authorization",
        "Bearer " +
          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3MzYwNTAxLCJpYXQiOjE3MDczNTMzMDEsImp0aSI6ImE2MjEzMWY0OTQxYTQ5YzhiOGZiOTUwMGVhNWMxZWVmIiwidXNlcl9pZCI6OH0.m1Uj7AA7XREEB7Oa-i9JJHDltPfXxsfAx8GOq3MvYv0"
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
    updateProperty: builder.mutation({
      query: (property) => {
        console.log(property);
        return {
          url: `update/${property["slug"]}`,
          method: "PUT",
          body: {
            property,
          },
          credentials: "include",
        };
      },
    }),
    getProperty: builder.query({
      query: (property) => {
        return {
          url: `details/${property["slug"]}`,
          method: "GET",
          credentials: "include",
        };
      },
    }),
    deleteProperty: builder.mutation({
      query: (property) => {
        return {
          url: `delete/${property["slug"]}`,
          method: "DELETE",
          credentials: "include",
        };
      },
    }),
    getPorpertyDetails: builder.query({
      query: (slug) => {
        return {
          url: `details/${slug}`,
          method: "GET",
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
  useUpdatePropertyMutation,
  useGetPropertyQuery,
  useDeletePropertyMutation,
  useGetPorpertyDetailsQuery,
} = propertiesApi;
