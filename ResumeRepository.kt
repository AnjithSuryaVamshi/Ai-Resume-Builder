package com.example.resumeenhancer.data

import kotlinx.coroutines.flow.Flow

class ResumeRepository(private val resumeDao: ResumeDao) {

    // Get all resumes as Flow (Live Data for Compose)
    val allResumes: Flow<List<ResumeEntity>> = resumeDao.getAllResumes()

    // Insert Resume
    suspend fun insert(resume: ResumeEntity) {
        resumeDao.insertResume(resume)
    }

    // Delete Resume
    suspend fun delete(resume: ResumeEntity) {
        resumeDao.deleteResume(resume)
    }
}
