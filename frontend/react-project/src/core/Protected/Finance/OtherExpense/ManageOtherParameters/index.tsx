import React from "react";
import Form from "./Form";
import List from "./List";

interface Props {}

const ManageOtherParameters = (props: Props) => {
  const [editData, setEditData] = React.useState<any>();

  return (
    <div>
      <Form editData={editData} />

      <List setEditData={setEditData} />
    </div>
  );
};

export default ManageOtherParameters;
