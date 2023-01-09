import { gql } from '@apollo/client';

const CREATE_ISSUE = gql`mutation createIssue($issueInput: IssueInput!) { createIssue(issueInput: $issueInput) { id title description createdAt answer } }`

const DELETE_ISSUE = gql`mutation deleteIssue($ID: ID!) { deleteIssue(ID: $ID) }`

const EDIT_ISSUE = gql`mutation editIssue($ID: ID!, $issueInput: IssueInput!) { editIssue(ID: $ID, issueInput: $issueInput) { answer } }`

export { CREATE_ISSUE, DELETE_ISSUE, EDIT_ISSUE};