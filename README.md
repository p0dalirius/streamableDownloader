# streamableDownloader

<p align="center">
    A simple python script to download videos hosted on streamable from their link.
    <br>
    <img src="https://badges.pufler.dev/visits/p0dalirius/streamableDownloader/"/>
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/streamableDownloader">
    <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
</p>



## Streamable

![](./.github/streamable.png)

## The technique

Extract the video URLs from the meta tags for opengraph:

```html
<meta property="og:url" content="https://streamable.com/abcdef" />
<meta property="og:video" content="https://cdn-cf-east.streamable.com/video/mp4/abcdef.mp4?Expires=1642074961&Signature=NrOSgEjyOX51sLshgTMtDEShsC97cusGrQKr87hRbJe8NNP8gobxxmqgxaFTakaM5xK6Ykw8K32DLLTbJHO9A5KeGJG2mFvjbYfVPAp07qSd93g6LsesEmqWmnEZHH7MRyAYhq4cYWtQRekFdnsn0JtWvMoAMWI4IUG3nMrkb47tsSYY5XtfYN5KzaTAzh4UrgsyzDVofCVqGYxXR1KpU35hQFtiRan5i0GfFDXfv5YqJ1davybrY3Eygcpk7WJBA6yMtv5uuN6GbWRWvsyVypXFo2kw8NNUbheGgXXHLISaQqbYowMY5NGaX3O1G6uQ7htctIIcDXw13NDggXk4CL__&Key-Pair-Id=WXADY4C7RJIBPIOFRBWM">
<meta property="og:video:url" content="https://cdn-cf-east.streamable.com/video/mp4/abcdef.mp4?Expires=1642074961&Signature=NrOSgEjyOX51sLshgTMtDEShsC97cusGrQKr87hRbJe8NNP8gobxxmqgxaFTakaM5xK6Ykw8K32DLLTbJHO9A5KeGJG2mFvjbYfVPAp07qSd93g6LsesEmqWmnEZHH7MRyAYhq4cYWtQRekFdnsn0JtWvMoAMWI4IUG3nMrkb47tsSYY5XtfYN5KzaTAzh4UrgsyzDVofCVqGYxXR1KpU35hQFtiRan5i0GfFDXfv5YqJ1davybrY3Eygcpk7WJBA6yMtv5uuN6GbWRWvsyVypXFo2kw8NNUbheGgXXHLISaQqbYowMY5NGaX3O1G6uQ7htctIIcDXw13NDggXk4CL__&Key-Pair-Id=WXADY4C7RJIBPIOFRBWM">
<meta property="og:video:secure_url" content="https://cdn-cf-east.streamable.com/video/mp4/abcdef.mp4?Expires=1642074961&Signature=NrOSgEjyOX51sLshgTMtDEShsC97cusGrQKr87hRbJe8NNP8gobxxmqgxaFTakaM5xK6Ykw8K32DLLTbJHO9A5KeGJG2mFvjbYfVPAp07qSd93g6LsesEmqWmnEZHH7MRyAYhq4cYWtQRekFdnsn0JtWvMoAMWI4IUG3nMrkb47tsSYY5XtfYN5KzaTAzh4UrgsyzDVofCVqGYxXR1KpU35hQFtiRan5i0GfFDXfv5YqJ1davybrY3Eygcpk7WJBA6yMtv5uuN6GbWRWvsyVypXFo2kw8NNUbheGgXXHLISaQqbYowMY5NGaX3O1G6uQ7htctIIcDXw13NDggXk4CL__&Key-Pair-Id=WXADY4C7RJIBPIOFRBWM">
```

## Example

```
bash$ ./streamableDownloader.py -u https://streamable.com/abcdef -o video.mp4
[>] Downloading to video.mp4 ...
[>] Downloaded 16.78 MB to video.mp4 ...
```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.
