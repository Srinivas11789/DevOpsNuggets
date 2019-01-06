package main

import (
        "os"
	"fmt"
        "io/ioutil"

	"github.com/docker/docker/api/types"
	"github.com/docker/docker/client"
        "github.com/jhoonb/archivex"
        "context"
)

func main() {

        // Docker Client Object
	//cli, err := client.NewEnvClient() "unix:///var/run/docker.sock", "v1.22", nil, nil
        cli, err := client.NewClient("unix:///var/run/docker.sock", "v1.35", nil, nil)

        // Docker Client error handle
	if err != nil {
		panic(err)
	}

        // Current directory path
        path, _  := os.Getwd()

        // Create tar file of the folder
        tar := new(archivex.TarFile)
        tar.Create("<name_of_tar_file>.tar")
        tar.AddAll(path+"/<folder_name_containing_dockerfile>", false)
        tar.Close()

        // Tar file handle 
        dockerBuildContext, err := os.Open("<name_of_tar_file>.tar")
        defer dockerBuildContext.Close()

        // Build Docker Image
        //image := types.ImageBuildOptions{
        //  Dockerfile:   path,
        //}
        options := types.ImageBuildOptions{
        //SuppressOutput: false,
        Remove:         true,
        ForceRemove:    true,
        PullParent:     true}

        //fmt.Println(image)

        ctx := context.Background()

        buildResponse, err := cli.ImageBuild(ctx, dockerBuildContext, options)

        if err != nil {
            fmt.Printf("Error, %v", err)
        }

        fmt.Printf("********* %s **********", buildResponse.OSType)
        response, err := ioutil.ReadAll(buildResponse.Body)
        if err != nil {
            fmt.Printf("%s", err.Error())
        }
        fmt.Println(string(response))

}
// Reference:
// * https://stackoverflow.com/questions/38804313/build-docker-image-from-go-code
// * https://github.com/moby/moby/issues/27186
