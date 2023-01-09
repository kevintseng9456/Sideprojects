import mongoose from "mongoose";

const issueSchema = new mongoose.Schema({
    title: String,
    description: String,
    createdAt: String,
    answer: Boolean,
  });
  
const Issue = mongoose.model('Issue', issueSchema);

export default Issue