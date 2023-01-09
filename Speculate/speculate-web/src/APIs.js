import { useMutation, useQuery } from '@apollo/client';
import { CREATE_ISSUE, DELETE_ISSUE, EDIT_ISSUE} from './mutations';
import {GET_ISSUES} from './querys'

function APIs() {
    // 在這裡定義您的 useMutation Hook
    const [createIssue] = useMutation(CREATE_ISSUE);
    const [deleteIssue] = useMutation(DELETE_ISSUE);
    const [editIssue] = useMutation(EDIT_ISSUE);

    // 取得資料
    const {loading, error, data} = useQuery(GET_ISSUES);

    // 使用這些 Hook
    async function handleCreateIssue(issueInput) {
    const { data } = await createIssue({ variables: { issueInput } });
    console.log(data);
    }

    async function handleDeleteIssue(ID) {
    const { data } = await deleteIssue({ variables: { ID } });
    console.log(data);
    }

    async function handleEditIssue(issueID, answer) {
    const { data } = await editIssue({ variables: { ID: issueID, issueInput: {answer}  } });
    console.log(data);
    }


    if (loading) return <p>Loading...</p>;
    if (error) return <p>Something Went Wrong</p>;


    return {
        createIssue: handleCreateIssue,
        deleteIssue: handleDeleteIssue,
        editIssue: handleEditIssue,
        getIssues: !loading && !error && data.getIssues
    };
}

export default APIs;

